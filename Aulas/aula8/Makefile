all: tweets.model

tweets_shuffled.csv: tweets.csv
	shuf $< -o $@

tweets_train.csv: tweets_shuffled.csv
	head -n 500000 $< > $@

tweets_test.csv: tweets_shuffled.csv
	tail -n +500000 $< > $@

tweets.model: tweets_train.csv tweets_test.csv main.py
	python main.py