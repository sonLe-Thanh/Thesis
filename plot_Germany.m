data_uci = load("Data/Result/Germany_50_result_uci.csv");
data_umass = load("Data/Result/Germany_50_result_umass.csv");

plot(data_uci(:,1), data_uci(:,2), "-r", "linewidth",2);
hold on

plot(data_umass(:,1), data_umass(:,2), "-b", "linewidth",2);


xlabel("Number of topics", "FontSize", 20);
ylabel("Topic coherence", "FontSize", 20);

title("Topic coherence with different number of topics", "FontSize", 25);
legend(["UCI","UMass"], "FontSize", 17);

hold off 

% 73 for Germany