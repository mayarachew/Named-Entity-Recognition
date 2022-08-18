from sklearn.model_selection import train_test_split

SEED_VAL = 42


def print_percentage(X, dataset):

    percentage = len(X[dataset])*100 / (len(X['test']) +
                                        len(X['train']) + len(X['val']))
    print(f'{dataset}: {round(percentage)}%')

    return


def split_dataset(X_padded, y_padded):
    X = {}
    y = {}

    # for classification
    X['train'], X['test'], y['train'], y['test'] = train_test_split(X_padded, y_padded, test_size=0.2, random_state=SEED_VAL)
    X['train'], X['val'], y['train'], y['val'] = train_test_split(X['train'], y['train'], test_size=0.125, random_state=SEED_VAL)

    print_percentage(X, 'train')
    print_percentage(X, 'val')
    print_percentage(X, 'test')

    return X, y


def prepare_to_eval(idx_tag_dict, y_true, y_pred):
  pred_tag = []
  real_tag = []
  
  for text in y_pred:
    tags_text = []
    for palavra in text:
      tags_text.append(idx_tag_dict[palavra])
    pred_tag.append(tags_text)

  for text in y_true:
    tags_text = []
    for palavra in text:
      tags_text.append(idx_tag_dict[palavra])
    real_tag.append(tags_text)
  
  return real_tag, pred_tag
