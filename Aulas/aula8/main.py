import fasttext

try:
    model = fasttext.load_model('tweets.model')
except ValueError:
    model = fasttext.train_supervised(input="tweets_train.csv", dim=300)
    model.save_model('tweets.model')

print(model.test('tweets_test.csv'))
strings = [
 "passei no exame de condução",
 "chumbei no exame de condução",
 "reprovei no exame de condução",
 "hoje choveu torrencialmente",
 "hoje está um lindo sol",
 "ontem comi uma pizza saborosa"
]

for string in strings:
    print(string + ":")
    print(model.predict(string, k=2),'\n')
    