data_umass = load("Data/Result/China_50_result_umass.csv");
data_perplexity_train = load("Data/Result/China_50_result_perplexity_train.csv");
data_perplexity_test = load("Data/Result/China_50_result_perplexity_test.csv");

f1 = figure;
plot(data_umass(:,1), data_umass(:,2), "-b", "linewidth",2);
xlabel("Number of topics", "FontSize", 20);
ylabel("Umass", "FontSize", 20);

title("Topic coherence (Umass) with different number of topics");
legend('Umass', "FontSize", 17);

f2 = figure;
plot(data_perplexity_train(:, 1), data_perplexity_train(:, 2), "-b", data_perplexity_test(:, 1), data_perplexity_test(:, 2), "-r", "linewidth", 2);
xlabel("Number of topics", "FontSize", 20);
ylabel("Perplexity", "FontSize", 20);

title("Topic coherence (Perplexity) with different number of topics");
legend(["Train", "Test"], "FontSize", 17);


% 77 for France 
% 90 for China
% 79 for Germany
% 82 for Japan
% 92 for Korea
% 76 for Vietnam