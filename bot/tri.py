def get_head_from_question(question="", predicate=""):
    index = question.find(predicate)
    if index == -1:
        return None
    else:
        return question[:index - 1]


def get_head_predicate_from_question(question="", label='0', predicate_list=['str']):
    predicates = predicate_list[int(label)].split(",")
    for predicate in predicates:
        index = question.find(predicate)
        if index > -1:
            head = question[:index].strip()
            return (head, predicate)
    return (None, None)


def get_tail_from_triples(triples, head, predicate):
    head_predicate = "{}#{}".format(head, predicate)
    for triple in triples:
        if head_predicate in triple:
            return triple[len(head_predicate) + 1:]
    return None


def get_tail_from_triples_nn(triples_nn, head):
    for triple in triples_nn:
        if head in triple:
            return triple[len(head) + 1:]
    return None


# def predicates_filter(label='0', predicates_list=[]):
#     result = []
#     list1 = list(filter(lambda predicates: predicates.startswith(label + '#'), predicates_list))
#     for label_predicate in list1:
#         result.append(label_predicate.split('#')[1])
#     return result

def get_tail_from_triples3(triples, head, predicate, word2vec_model):
    head_predicate_input = "{} {}".format(head, predicate)
    sim = 0
    sim_head_predicate = ""
    tail = ""
    for triple in triples:
        parts = triple.split("#")
        head_predicate = parts[0] + ' ' + parts[1]
        temp = word2vec_model.similarity(head_predicate_input, head_predicate)
        if temp > sim:
            sim = temp
            sim_head_predicate = head_predicate
            tail = parts[2]
    print("***{}#{}#{}".format(sim, sim_head_predicate, tail))
    return tail