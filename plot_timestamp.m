COUNTRY = ["China"; "France"; "Germany"; "Japan"; "Korea"; "Vietnam"];
TIMESTAMP = ["pre2018"; "2018"; "2019"; "2020"; "2021"];

n_countries = 6;
n_timestamp = 5;
n_iteraions = 50;
file = [];
topic = [];
for i=1:n_countries
    for j=1:n_timestamp
        country = COUNTRY(i);
        timestamp = TIMESTAMP(j);

        file_umass_result = "Data/Result_timestamp/" + country + "_" + timestamp + "_" + n_iteraions + "_result_umass.csv";
        data_umass = load(file_umass_result);

        [argvalue, argmax] = max(data_umass(:,2));

        file = [file; file_umass_result];
        topic = [topic; argmax + 39];
    end
end

T = table(file, topic);
writetable(T,'topic_timestamp.txt');