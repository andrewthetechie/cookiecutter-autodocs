import yaml
import argparse


def main(entrypoint: str, index: int):
    with open(".pre-commit-hooks.yaml") as fh:
        hooks = yaml.safe_load(fh)

    hooks[index]["entry"] = f"/cookiecutter-autodocs {entrypoint}"
    hooks[index]["language"] = "docker"
    hooks[index][args] = []

    with open(".pre-commit-hooks.yaml", "w") as fh:
        yaml.dump(hooks, fh)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("entrypoint")
    parser.add_argument("index")

    args = parser.parse_args()
    main(entrypoint=args.entrypoint, index=int(args.index))
