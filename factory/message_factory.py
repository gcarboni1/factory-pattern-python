from inspect import getmembers, isclass, isabstract

import messages


class RowsFactory:
    class_map = []

    def __init__(self, ):
        self.class_map = self.create_class_map()

    def create_class_map(self):
        class_list = []

        concrete_classes = getmembers(messages,
              lambda m: isclass(m)
                        and not isabstract(m)
                        and issubclass(m, messages.CsvRow)
              )

        for class_name, concrete_class in concrete_classes:
            class_list.append(dict(
                class_name=class_name,
                concrete_class=concrete_class
            ))
        return class_list

    def create_row_instance(self, class_name, csv_line):
        row_class = list(filter(
                lambda elem: elem.get("class_name") == class_name,
                self.class_map
        ))

        if (len(row_class)) == 0:
            raise Exception(f"No fabric found with this name: {class_name}")

        return row_class[0].get("concrete_class")(csv_line)
