from models.Node import Node
from models.LinkedList import LinkedList


def main():

    lig_list = LinkedList()
    while True:
        valores = input.split(" ")

        match valores[0]:
            case "RPI":
                lig_list.insert_at_start(valores[1])
                print(lig_list)
            case "RPF":
                lig_list.insert_at_end(valores[1])

            case "RPDE":
                lig_list.insert_before_item(valores[1],valores[2])

            case "RPAE":
                lig_list.insert_after_item(valores[1],valores[2])

            case "RDII":
                lig_list.insert_at_index(valores[1],valores[2])

            case "VNE":
                lig_list.get_count

            case "VP":
                lig_list.search_item(valores[1])

            case "EPE":
                lig_list.delete_at_start

            case "EUE":
                lig_list.delete_at_end

            case "EP":
                lig_list.delete_element_by_value(valores[1])
