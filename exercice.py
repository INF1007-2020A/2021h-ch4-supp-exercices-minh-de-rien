#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
	if len(string) % 2 == 0:
		return 0xDEADBEEF

	return False


def get_num_char(string, char):
	nbr_occurrence = 0

	for c in string:
		if c == char:
			nbr_occurrence += 1 # nbr_occurrence += 1 if c == char else 0

	return nbr_occurrence


def get_first_part_of_name(name):
	full_first_name = name.split("-")

	return full_first_name[0][0].upper() + full_first_name[0][1:]


def get_random_sentence(animals, adjectives, fruits):
	return f"Aujourd'hui, j'ai vu un {random.choice(animals)} s'emparer d'un panier {random.choice(adjectives)} plein de {random.choice(fruits)}"


if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
