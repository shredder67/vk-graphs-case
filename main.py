import argparse
from model import CharityClassifier
from train_util import train_model, get_subm_predictions


def main():
    predictor = CharityClassifier()
    train_model(predictor)
    subm_preds = get_subm_predictions()
    subm_preds.to_csv('submission.csv')


if __name__ == '__main__':
    main()