import numpy as np
from scipy.special import psi, polygamma, loggamma


class LdaModel:
    def __init__(self, docs, num_topics, vocabulary):
        self.docs = docs # a matrix of size M x N_d
        self.K = num_topics # a number K
        self.vocabulary = vocabulary # a list of word in ABC order
        self.M = len(self.docs)
        self.N = np.array(list(map(lambda x: len(x), self.docs)))
        self.V = len(vocabulary)

        # parameter
        np.random.seed(1)
        self.alpha = np.random.gamma(shape=100, scale=0.01, size=self.K)
        self.beta = np.random.dirichlet(np.ones(self.V), self.K)
        self.phi = np.ones((self.M, np.max(self.N), self.K)) / self.K # LDA paper
        for d, n in enumerate(self.N):
            self.phi[d, n:, :] = 0
        self.gamma = self.alpha + np.ones((self.M, self.K)) * self.N.reshape(-1, 1) / self.K
        np.set_printoptions(precision=4)

    def e_step(self, iterations=50):
        for d in range(self.M):
            # update Phi
            self.phi[d, :self.N[d], :] = self.beta[:, self.docs[d]].T * \
                                         np.exp(psi(self.gamma[d, :]) - psi(self.gamma[d, :].sum()))

            # normalize phi
            self.phi[d, :self.N[d]] /= self.phi[d, :self.N[d]].sum(axis=1).reshape(-1, 1)
        # update gamma
        self.gamma = self.alpha + self.phi.sum(axis=1)

    def m_step(self):
        # update beta
        for i in range(self.V):
            self.beta[:, i] = np.array([
                (np.array(self.docs[d]) == i) @ self.phi[d, :self.N[d], :] for d in range(self.M)
            ]).sum(axis=0)
        # normalize beta
        self.beta /= self.beta.sum(axis=1).reshape(-1, 1)

        # update alpha: Newton-Raphson
        self.newton_raphson()

    def newton_raphson(self, max_iter=10000, eps=1e-2):
        for _ in range(max_iter):
            alpha = self.alpha.copy()
            # gradient
            g = self.M * (psi(self.alpha.sum()) - psi(self.alpha)) \
                + (psi(self.gamma) - psi(self.gamma.sum(axis=1)).reshape(-1, 1)).sum(axis=0)
            # hessian matrix: H = diag(h) + 1z1^T
            # Compute Newton step: d = -(H^-1g) = -(g-c)/h
            z = self.M * polygamma(1, self.alpha.sum())
            h = -self.M * polygamma(1, self.alpha)
            c = (g / h).sum() / (1./z + (1./h).sum())
            d = -(g - c) / h
            self.alpha += d

            # check convergence
            err = np.linalg.norm(self.alpha - alpha)
            # print(f"{_}", err)
            if  err < eps:
                break

    def train(self, max_iter=100, eps=3e-2):
        lb_old = -np.inf
        for it in range(max_iter):
            self.e_step()
            self.m_step()
            lb = self.elbo()
            err = abs(lb - lb_old)
            lb_old = lb
            print(f"{it: 04}:  ELBO: {lb: .4f},  error: {err: .3f}")
            if err < eps:
                break
        print("Beta", self.beta)

    def elbo(self):
        lb = 0
        for d in range(self.M):
            lb = lb + loggamma(self.alpha.sum()) - loggamma(self.alpha).sum() \
               + ((self.alpha - 1)*(psi(self.gamma[d, :]) - psi(self.gamma[d, :].sum()))).sum()

            lb += (self.phi[d, :self.N[d], :] * (psi(self.gamma[d, :]) - psi(self.gamma[d, :].sum()))).sum(axis=1).sum(axis=0)

            lb += (self.phi[d, :self.N[d], :] * np.log(self.beta[:, self.docs[d]].T)).sum(axis=1).sum(axis=0)

            lb -= loggamma(self.gamma[d, :].sum()) - loggamma(self.gamma[d, :]).sum() \
               + ((self.gamma[d, :] - 1)*(psi(self.gamma[d, :]) - psi(self.gamma[d, :].sum()))).sum()

            lb -= (self.phi[d, :self.N[d], :] * np.log(self.phi[d, :self.N[d], :])).sum(axis=1).sum(axis=0)
        # return lb / self.M
        return lb

    def show_topics(self, n=10):
        """
        find the index of the largest `n` values in a list
        """
        for k in range(self.K):
            max_values = self.beta[k].argsort()[-n:][::-1]
            topic_k =  np.array(list(self.vocabulary.keys()))[max_values]
            print(f"Topic {k:02}: {topic_k}")
            print(max_values)


def main():
    corpus = [
        "skyscrapers higher eiffel",
        "visit eiffel go paris",
        "charming heart paris"
    ]
    vocabulary = {
        "skyscrapers": 0,
        "higher": 1,
        "eiffel": 2,
        "visit": 3,
        "go": 4,
        "paris": 5,
        "charming": 6,
        "heart": 7
    }
    docs = [[vocabulary[word] for word in doc.split(' ')] for doc in corpus]
    lda_model = LdaModel(docs=docs, num_topics=2, vocabulary=vocabulary)
    lda_model.train()
    lda_model.show_topics(n=3)


if __name__ == "__main__":
    main()
