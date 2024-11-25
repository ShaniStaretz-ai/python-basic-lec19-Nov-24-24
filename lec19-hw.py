oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman",
                 "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth",
                   "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

# a
oscar_winners.add("Emma Watson")
print("added Emma Watson:\n", oscar_winners)
# b
oscar_winners_copy = oscar_winners.copy()
oscar_winners_copy.remove("Meryl Streep")
print("removed Meryl Streep:\n", oscar_winners_copy)
oscar_winners_copy.clear()
print("clear oscar_winners_copy:\n", oscar_winners_copy)
# c
print(
    f"common in titanic and dark knight:\n {titanic_actors & dark_knight_actors if len(titanic_actors & dark_knight_actors) else None}")
# d
print(f"is there common actors in iron man and avengers:\n {not iron_man_actors.isdisjoint(avengers_actors)}")
# e
print(f"is all actors list won the oscar:\n {actor_list <= oscar_winners}")
# f
print(f"is all actors list contains all actors in the avengers:\n {actor_list > avengers_actors}")
# g
if len(movie_cast):
    print(f"random removed '{movie_cast.pop()}' from movie_cast set")
    print("after random removed:", movie_cast)
# h
if "Matt Damon" in movie_cast:
    movie_cast.remove("Matt Damon")
    print("removed Matt Damon:", movie_cast)
# i
print(f"actors did not win the oscar are:\n {titanic_actors - oscar_winners}")
# j
print(
    f"actors played in titanic or dark knight:\n {titanic_actors ^ dark_knight_actors}")  # doesn't have in common so all actors in both sets
# k
oscar_winners.update({"Cate Blanchett", "Daniel Day-Lewis"})
print("after adding 'Cate Blanchett' and 'Daniel Day-Lewis':\n", oscar_winners)
# l
print("after unite titanic and dark knight actors':\n", titanic_actors | dark_knight_actors)
