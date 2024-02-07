class Relation:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)

    def is_reflexive(self):
        for i in range(self.size):
            if not self.matrix[i][i]:
                return False
        return True

    def is_symmetric(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def is_antisymmetric(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] and self.matrix[j][i] and i != j:
                    return False
        return True

    def is_transitive(self):
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    if self.matrix[i][j] and self.matrix[j][k] and not self.matrix[i][k]:
                        return False
        return True

    def check_relation_type(self):
        if self.is_reflexive() and self.is_symmetric() and self.is_transitive():
            return "Equivalence Relation"
        elif self.is_reflexive() and self.is_antisymmetric() and self.is_transitive():
            return "Partial Order Relation"
        else:
            return "None"


def main():
    # Example usage:
    matrix = [
        [1, 0, 0],
        [0, 1, 0],
        [1, 0, 1]
    ]
    relation = Relation(matrix)

    print("Reflexive:", relation.is_reflexive())
    print("Symmetric:", relation.is_symmetric())
    print("Anti-symmetric:", relation.is_antisymmetric())
    print("Transitive:", relation.is_transitive())
    print("Relation type:", relation.check_relation_type())


if __name__ == "__main__":
    main()
