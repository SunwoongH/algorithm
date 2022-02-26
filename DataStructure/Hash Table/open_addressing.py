class OpenAddressing:
    DELETED = 'deleted'
    def __init__(self, n: int):
        self.__table = [None for _ in range(n)]
        self.__size = 0
        
    def _hash_function(self, i: int, key) -> int:
        return (key + i) % len(self.__table)
    
    def search(self, key):
        for i in range(len(self.__table)):
            hash = self._hash_function(i, key)
            if not self.__table[hash]:
                return
            elif self.__table[hash] != OpenAddressing.DELETED and self.__table[hash][0] == key:
                return self.__table[hash][1]
    
    def insert(self, key, value) -> None:
        if self.is_full():
            return
        for i in range(len(self.__table)):
            hash = self._hash_function(i, key)
            if not self.__table[hash] or self.__table[hash] == OpenAddressing.DELETED:
                self.__table[hash] = (key, value)
                self.__size += 1
                break
            
    def delete(self, key) -> None:
        for i in range(len(self.__table)):
            hash = self._hash_function(i, key)
            if not self.__table[hash]:
                return 
            elif self.__table[hash] != OpenAddressing.DELETED and self.__table[hash][0] == key:
                self.__table[hash] = OpenAddressing.DELETED
                self.__size -= 1
                break
    
    def is_full(self) -> bool:
        return self.__size == len(self.__table)
            
    def __getitem__(self, key):
        return self.search(key)
    
    def __setitem__(self, key, value):
        self.insert(key, value)