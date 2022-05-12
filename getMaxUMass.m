data_umass_pre2018 = load("Data/Result_timestamp/Vietnam_pre2018_50_result_umass.csv");
data_umass_2018 = load("Data/Result_timestamp/Vietnam_2018_50_result_umass.csv");
data_umass_2019 = load("Data/Result_timestamp/Vietnam_2019_50_result_umass.csv");
data_umass_2020 = load("Data/Result_timestamp/Vietnam_2020_50_result_umass.csv");
data_umass_2021 = load("Data/Result_timestamp/Vietnam_2021_50_result_umass.csv");

max_arr = zeros(5,1);
[val, idx] = max(data_umass_pre2018(:,2));

max_arr(1) = data_umass_pre2018(idx,1);

[val, idx] = max(data_umass_2018(:,2));

max_arr(2) = data_umass_2018(idx,1);

[val, idx] = max(data_umass_2019(:,2));

max_arr(3) = data_umass_2019(idx,1);

[val, idx] = max(data_umass_2020(:,2));

max_arr(4) = data_umass_2020(idx,1);

[val, idx] = max(data_umass_2021(:,2));

max_arr(5) = data_umass_2021(idx,1);

disp(max_arr);