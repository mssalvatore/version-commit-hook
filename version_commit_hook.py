import argparse
import tomllib


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    if "VERSION" in args.filenames or "pyproject.toml" in args.filenames:
        pyproject_version = read_pyproject_toml_version()
        version_version = read_version()

        if pyproject_version != version_version:
            print(
                "VERSION file does not match pyproject.toml version: "
                f"{version_version} != {pyproject_version}"
            )
            exit(1)


def read_version() -> str:
    with open("VERSION") as f:
        return f.read().strip()


def read_pyproject_toml_version() -> str:
    with open("pyproject.toml", "rb") as f:
        return tomllib.load(f)["tool"]["poetry"]["version"].strip(" v")


if __name__ == "__main__":
    main()
