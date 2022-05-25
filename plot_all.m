COUNTRY = ["China"; "France"; "Germany"; "Japan"; "Korea"; "Vietnam"];

n_countries = 6;
file = [];
topic = [];
for i=1:n_countries
        country = COUNTRY(i);
        timestamp = TIMESTAMP(j);

        file_umass_result = "Data/NMF/Result/" + country + "_result_umass.csv";
        data_umass = load(file_umass_result);

        [argvalue, argmax] = max(data_umass(:,2));

        file = [file; file_umass_result];
        topic = [topic; argmax + 39];
end

T = table(file, topic);
writetable(T,'NMF_topic_all.txt');
