class Node:
    def parts_str(self):
        st = []
        for part in self.parts:
            st.append( str( part ) )
        return "\n".join(st)

    def __repr__(self):
        if self.type == 'STMT_LIST':
            return self.parts_str().replace("\n", "\n")
        else:
            return self.type + ":\n\t" + self.parts_str().replace("\n", "\n\t")

    def add_parts(self, parts):
        self.parts += parts
        return self

    def __init__(self, type, parts, row=-1):
        self.type = type
        self.parts = parts
        self.row_pos = row
