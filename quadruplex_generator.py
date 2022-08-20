import exrex

import random
from typing import List


class QuadruplexGenerator:
    """
    Quadruplex generator, uses all available detection regexes to generate
    new sequences containing quadruplexes.

    Source: Emilia Puig Lombardi, Arturo Londoño-Vallejo, A guide to computational methods for G-quadruplex prediction, Nucleic Acids Research, Volume 48, Issue 1, 10 January 2020, Pages 1–15, https://doi.org/10.1093/nar/gkz1097
    """

    REGEX_LIST: List[str] = [
        "G{3,5}[ATC]{1,7}G{3,5}[ATC]{1,7}G{3,5}[ATC]{1,7}G{3,5}",
        "G{3,5}[ATC]{1,7}C{3,5}[ATC]{1,7}G{3,5}[ATC]{1,7}C{3,5}",
        "G{3,5}[ATC]{1,7}G{3,5}[ATC]{1,7}C{3,5}[ATC]{1,7}C{3,5}",
        "G{3,5}[ATC]{1,7}C{3,5}[ATC]{1,7}C{3,5}[ATC]{1,7}G{3,5}",
        "G{3,5}[ATC]{1,7}G{3,5}[ATC]{1,7}G{3,5}[ATC]{1,7}C{3,5}",
        "G{3,5}[ATC]{1,7}G{3,5}[ATC]{1,7}C{3,5}[ATC]{1,7}G{3,5}",
        "C{3,5}[ATC]{1,7}C{3,5}[ATC]{1,7}C{3,5}[ATC]{1,7}C{3,5}",
        "C{3,5}[ATC]{1,7}G{3,5}[ATC]{1,7}C{3,5}[ATC]{1,7}G{3,5}",
        "C{3,5}[ATC]{1,7}C{3,5}[ATC]{1,7}G{3,5}[ATC]{1,7}G{3,5}",
        "C{3,5}[ATC]{1,7}G{3,5}[ATC]{1,7}G{3,5}[ATC]{1,7}C{3,5}",
        "C{3,5}[ATC]{1,7}C{3,5}[ATC]{1,7}C{3,5}[ATC]{1,7}G{3,5}",
        "C{3,5}[ATC]{1,7}C{3,5}[ATC]{1,7}G{3,5}[ATC]{1,7}C{3,5}",
    ]
    NOISE_NUCLEOTIDES: List[str] = ["A", "T"]

    def __init__(self) -> None:
        self.quadruplexes: List[str] = []

    def _place_random_noise(
        self,
        *,
        sequence: str,
        minimum_number_of_noise: int,
        maximum_number_of_noise: int,
    ) -> str:
        """
        Generate random random noise to the sequence
        :param sequence: generated sequence
        :param minimum_number_of_noise: minimum number of noise nucleotides
        :param maximum_number_of_noise: maximum number of noise nucleotides
        :return: sequence with random noise
        """
        sequence = list(sequence)
        places = random.randint(minimum_number_of_noise, maximum_number_of_noise)

        for i in range(places):
            index = random.randint(1, len(sequence))

            if index < len(sequence):
                sequence[index] = random.choice(self.NOISE_NUCLEOTIDES)

        return "".join(sequence)

    def _generate_quadruplexes(
        self,
        *,
        quadruplex_regex: str,
        limit: int,
        place_random_noise: bool = False,
        minimum_number_of_noise: int,
        maximum_number_of_noise: int,
    ) -> List[str]:
        """
        Generate quadruplex sequences base on regex.
        :param quadruplex_regex: quadruplex detection regex used for generation
        :param limit: maximum number of generated quadruplexes per one regex
        :param place_random_noise: place random noise to the sequence
        :param minimum_number_of_noise: minimum number of noise nucleotides
        :param maximum_number_of_noise: maximum number of noise nucleotides
        :return: list of quadruplex sequences
        """
        local_quadruplexes: List[str] = []

        while len(local_quadruplexes) <= limit:
            generated_quadruplex = exrex.getone(quadruplex_regex)

            if generated_quadruplex not in local_quadruplexes:
                if place_random_noise:
                    local_quadruplexes.append(
                        self._place_random_noise(
                            sequence=generated_quadruplex,
                            minimum_number_of_noise=minimum_number_of_noise,
                            maximum_number_of_noise=maximum_number_of_noise,
                        )
                    )
                else:
                    local_quadruplexes.append(generated_quadruplex)

        return local_quadruplexes

    def run(
        self,
        *,
        limit_per_regex: int = 10,
        place_random_noise: bool = False,
        minimum_number_of_noise: int = 0,
        maximum_number_of_noise: int = 3,
    ) -> None:
        """
        Run quadruplex generator
        :param limit_per_regex: maximum number of generated quadruplexes per one regex
        :param place_random_noise: place random noise to the sequence
        :param minimum_number_of_noise: minimum number of noise nucleotides
        :param maximum_number_of_noise: maximum number of noise nucleotides
        :return:
        """

        for regex in self.REGEX_LIST:
            self.quadruplexes += self._generate_quadruplexes(
                quadruplex_regex=regex,
                limit=limit_per_regex,
                minimum_number_of_noise=minimum_number_of_noise,
                maximum_number_of_noise=maximum_number_of_noise,
                place_random_noise=place_random_noise,
            )


if __name__ == "__main__":
    generator = QuadruplexGenerator()
    generator.run(
        limit_per_regex=10,
        place_random_noise=True,
        minimum_number_of_noise=1,
        maximum_number_of_noise=3,
    )

    print(generator.quadruplexes)
