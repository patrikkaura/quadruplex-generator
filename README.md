<h1 align='center'> Quadruplex generator</h1>
<br />
<div align="center">
    <img src="https://img.shields.io/badge/Version 1.0.0-green?style=for-the-badge" alt='package_version'/>
    <img src="https://img.shields.io/badge/Python 3.7+-00599C?style=for-the-badge&logo=python&logoColor=white" alt='python_version'/>
    <img src="https://img.shields.io/badge/jupyter-gray?style=for-the-badge&logo=jupyter" alt='jupyter'/>
</div>
<br />

Quadruplex generator is python script used to generate artificial guanine quadruplex sequences.

## Requirements

Quadruplex generator was built with Python 3.7+.

## Installation

To run quadruplex generator run

```commandline
poetry install
```

## Generate G-quadruplexes

To generate G-quadruplexes withou artificial noise run.

```python
if __name__ == "__main__":
    generator = QuadruplexGenerator()
    generator.run(limit_per_regex=10)

    print(generator.quadruplexes)
```

If artificial noise is needed run

```python
if __name__ == "__main__":
    generator = QuadruplexGenerator()
    generator.run(
        limit_per_regex=10,
        place_random_noise=True,
        minimum_number_of_noise=1,
        maximum_number_of_noise=3,
    )

    print(generator.quadruplexes)
```

All generated quadruplexes are stored in class variable `quadruplexes`.

```python
print(generator.quadruplexes)

> [
    'GGGGGAGAGTGCCGGGGGATAACGGG', 
    'GGGACCAACAGGGGCGGGATACTTGGGG', 
    'GAGGAGGGGCACCAGGGGGTTCCAAAGGGGG', 
    'GGTGCGGGTTAGGGGCATTTAGGGG',
    ...
  ]
```

## Dependencies

* exrex = "^0.10.5"

## Authors

* **Patrik Kaura** - *Main developer* - [patrikkaura](https://gitlab.com/PatrikKaura/)

## License

This project is licensed under the MIT License - see the [
LICENSE
](
LICENSE
) file for details. 
