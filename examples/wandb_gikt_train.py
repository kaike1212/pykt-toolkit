import argparse
from wandb_train import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_name", type=str, default="assist2009")
    parser.add_argument("--model_name", type=str, default="gikt")
    parser.add_argument("--emb_type", type=str, default="qid")
    parser.add_argument("--save_dir", type=str, default="saved_model")

    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--fold", type=int, default=0)
    parser.add_argument("--learning_rate", type=float, default=1e-3)
    # model params
    # TODO
    parser.add_argument("--dropout", type=float, default=(0.2, 0.2))
    parser.add_argument("--emb_size", type=int, default=100)
    parser.add_argument("--hidden_dim", type=int, default=100)
    parser.add_argument("--size_q_neighbors", type=int, default=4)
    parser.add_argument("--size_s_neighbors", type=int, default=4)
    parser.add_argument("--aggregator", type=str, default="sum")

    parser.add_argument("--use_wandb", type=int, default=1)
    parser.add_argument("--add_uuid", type=int, default=1)
    args = parser.parse_args()

    params = vars(args)
    main(params)
