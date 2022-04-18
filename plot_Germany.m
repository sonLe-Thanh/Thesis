data_50 = load("Data/Germany_50_result.csv");
data_100 = load("Data/Germany_100_result.csv");


plot(data_50(:,1), data_50(:,2), "-r", "linewidth",2);
hold on
plot(data_100(:,1), data_100(:,2), "-b", "linewidth",2);
xlabel("Number of topics", "FontSize", 20);
ylabel("Topic coherence", "FontSize", 20);
title("Topic coherence with different number of topics", "FontSize", 25);
legend(["50 iterations", "100 iterations"], "FontSize", 17);

hold off 


% plot(data_50(:,1), data_50(:,3), "-r", "linewidth",2);
% hold on
% plot(data_100(:,1), data_100(:,3), "-b", "linewidth",2);
% xlabel("Number of topics", "FontSize", 20);
% ylabel("Execution time", "FontSize", 20);
% title("Execution time with different number of topics", "FontSize", 25);
% legend(["50 iterations", "100 iterations"], "FontSize", 17);
% 
% hold off 