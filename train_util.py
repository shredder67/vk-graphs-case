def _prep_data(pr_data:pd.Dataframe):
    mask = np.random.choice(pr_data.shape[0], size=.shape[0], replace=False)
    ratio = int(0.8 * len(mask))
    return train_dataset, val_dataset = pr_data.iloc[list(mask[:ratio])], pr_data.iloc[list(mask[ratio:])]
    

def subm_prediction():
    pass


def train_model():
    pass