class Set:
    def __init__(self, elements=None):
        if elements is None:
            self.elements = set()
        else:
            self.elements = elements

    def is_member(self, element):
        """
        Check whether an element belongs to the set.

        Parameters:
            element (any): The element to check.

        Returns:
            bool: True if the element is a member of the set, False otherwise.
        """
        return element in self.elements

    def powerset(self):
        """
        Generate the powerset of the set.

        Returns:
            list: List containing all subsets of the set (powerset).
        """
        from itertools import chain, combinations
        return list(chain.from_iterable(combinations(self.elements, r) for r in range(len(self.elements)+1)))

    def subset(self, other_set):
        """
        Check whether one set is a subset of another set.

        Parameters:
            other_set (Set): The other set to check for being a subset of.

        Returns:
            bool: True if the set is a subset of the other set, False otherwise.
        """
        return self.elements.issubset(other_set.elements)

    def union(self, other_set):
        """
        Compute the union of two sets.

        Parameters:
            other_set (Set): The other set to compute the union with.

        Returns:
            Set: A new set containing elements from both sets.
        """
        new_set = Set()
        new_set.elements = self.elements.union(other_set.elements)
        return new_set

    def intersection(self, other_set):
        """
        Compute the intersection of two sets.

        Parameters:
            other_set (Set): The other set to compute the intersection with.

        Returns:
            Set: A new set containing elements common to both sets.
        """
        new_set = Set()
        new_set.elements = self.elements.intersection(other_set.elements)
        return new_set

    def complement(self, universal_set):
        """
        Compute the complement of the set with respect to a universal set.

        Parameters:
            universal_set (Set): The universal set.

        Returns:
            Set: A new set containing elements not present in the original set.
        """
        new_set = Set()
        new_set.elements = universal_set.elements.difference(self.elements)
        return new_set

    def set_difference(self, other_set):
        """
        Compute the set difference between two sets.

        Parameters:
            other_set (Set): The other set to compute the difference with.

        Returns:
            Set: A new set containing elements present in the original set but not in the other set.
        """
        new_set = Set()
        new_set.elements = self.elements.difference(other_set.elements)
        return new_set

    def symmetric_difference(self, other_set):
        """
        Compute the symmetric difference between two sets.

        Parameters:
            other_set (Set): The other set to compute the symmetric difference with.

        Returns:
            Set: A new set containing elements present in either set but not in both.
        """
        new_set = Set()
        new_set.elements = self.elements.symmetric_difference(other_set.elements)
        return new_set

    def cartesian_product(self, other_set):
        """
        Compute the Cartesian product of two sets.

        Parameters:
            other_set (Set): The other set to compute the Cartesian product with.

        Returns:
            set: A set containing tuples representing the Cartesian product of the two sets.
        """
        return {(x, y) for x in self.elements for y in other_set.elements}


def display_menu():
    print("Menu:")
    print("1. Check if an element belongs to the set")
    print("2. Generate the powerset of the set")
    print("3. Check if a set is a subset of another set")
    print("4. Compute the union of two sets")
    print("5. Compute the intersection of two sets")
    print("6. Compute the complement of the set (with respect to a universal set)")
    print("7. Compute the set difference between two sets")
    print("8. Compute the symmetric difference between two sets")
    print("9. Compute the Cartesian product of two sets")
    print("0. Exit")


def get_set_from_input():
    elements_str = input("Enter the elements of the set (comma-separated): ")
    elements = set(elements_str.split(','))
    return Set(elements)


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '0':
            print("Exiting the program.")
            break
        elif choice == '1':
            element = input("Enter the element to check: ")
            set_instance = get_set_from_input()
            print(f"Is {element} a member of the set? {set_instance.is_member(element)}")
        elif choice == '2':
            set_instance = get_set_from_input()
            print("Powerset of the set:")
            print(set_instance.powerset())
        elif choice == '3':
            set1 = get_set_from_input()
            set2 = get_set_from_input()
            print(f"Is set1 a subset of set2? {set1.subset(set2)}")
        elif choice == '4':
            set1 = get_set_from_input()
            set2 = get_set_from_input()
            print("Union of set1 and set2:")
            print(set1.union(set2).elements)
        elif choice == '5':
            set1 = get_set_from_input()
            set2 = get_set_from_input()
            print("Intersection of set1 and set2:")
            print(set1.intersection(set2).elements)
        elif choice == '6':
            set_instance = get_set_from_input()
            universal_set = get_set_from_input()
            print("Complement of the set:")
            print(set_instance.complement(universal_set).elements)
        elif choice == '7':
            set1 = get_set_from_input()
            set2 = get_set_from_input()
            print("Set difference (set1 - set2):")
            print(set1.set_difference(set2).elements)
        elif choice == '8':
            set1 = get_set_from_input()
            set2 = get_set_from_input()
            print("Symmetric difference of set1 and set2:")
            print(set1.symmetric_difference(set2).elements)
        elif choice == '9':
            set1 = get_set_from_input()
            set2 = get_set_from_input()
            print("Cartesian product of set1 and set2:")
            print(set1.cartesian_product(set2))
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
