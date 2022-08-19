from tensorflow.keras import Model, Input
from tensorflow.keras.layers import LSTM, Embedding, Dense, Dropout
from tensorflow.keras.layers import TimeDistributed, Bidirectional
from tensorflow_addons.layers import CRF


def create_model_bilstmcrf(MAX_SENTENCE, VOCAB_SIZE, NUM_TAGS):
  embedding_dim=50
  lstm_units=30

  input_word = Input(shape=(MAX_SENTENCE,))

  model = Embedding(input_dim=VOCAB_SIZE+1, output_dim=embedding_dim, input_length=MAX_SENTENCE)(input_word)

  model = Bidirectional(LSTM(units=lstm_units, return_sequences=True))(model)
  model = Dropout(0.1)(model)

  model = TimeDistributed(Dense(50, activation="relu"))(model)  
  crf = CRF(NUM_TAGS)
  decoded_sequence, potentials, sequence_length, chain_kernel = crf(model)

  model = Model(input_word, potentials)

  return model


def create_model_bilstm(MAX_SENTENCE, VOCAB_SIZE, NUM_TAGS):
  embedding_dim=50
  lstm_units=30

  input_word = Input(shape=(MAX_SENTENCE,))

  model = Embedding(input_dim=VOCAB_SIZE+1, output_dim=embedding_dim, input_length=MAX_SENTENCE)(input_word)

  model = Bidirectional(LSTM(units=lstm_units, return_sequences=True))(model)
  model = Dropout(0.1)(model)

  out = Dense(NUM_TAGS, activation="softmax")(model)  
 
  model = Model(input_word, out)

  return model


def create_model_2bilstm(MAX_SENTENCE, VOCAB_SIZE, NUM_TAGS):
  embedding_dim=50
  lstm_units=30

  input_word = Input(shape=(MAX_SENTENCE,))

  model = Embedding(input_dim=VOCAB_SIZE+1, output_dim=embedding_dim, input_length=MAX_SENTENCE)(input_word)

  model = Bidirectional(LSTM(units=lstm_units, return_sequences=True))(model)
  model = Dropout(0.1)(model)
  
  model = Bidirectional(LSTM(units=lstm_units, return_sequences=True))(model)
  model = Dropout(0.1)(model)

  out = Dense(NUM_TAGS, activation="softmax")(model)  
 
  model = Model(input_word, out)

  return model


def create_model_lstm(MAX_SENTENCE, VOCAB_SIZE, NUM_TAGS):
  embedding_dim=50
  lstm_units=30

  input_word = Input(shape=(MAX_SENTENCE,))

  model = Embedding(input_dim=VOCAB_SIZE+1, output_dim=embedding_dim, input_length=MAX_SENTENCE)(input_word)

  model = LSTM(units=lstm_units, return_sequences=True)(model)
  model = Dropout(0.1)(model)

  out = Dense(NUM_TAGS, activation="softmax")(model)  
 
  model = Model(input_word, out)

  return model


def create_model_lstmcrf(MAX_SENTENCE, VOCAB_SIZE, NUM_TAGS):
  embedding_dim=50
  lstm_units=30

  input_word = Input(shape=(MAX_SENTENCE,))

  model = Embedding(input_dim=VOCAB_SIZE+1, output_dim=embedding_dim, input_length=MAX_SENTENCE)(input_word)

  model = Bidirectional(LSTM(units=lstm_units, return_sequences=True))(model)
  model = Dropout(0.1)(model)

  model = TimeDistributed(Dense(50, activation="relu"))(model)  
  crf = CRF(NUM_TAGS)
  decoded_sequence, potentials, sequence_length, chain_kernel = crf(model)

  model = Model(input_word, potentials)

  return model