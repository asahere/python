class pattern:
     def print_pattern(self,n):
          for i in range(1,n+1):
               line=" ".join(str(j)for j in range(1,i+1))
               line+=line[-2::-1]
               print(line.ljust(2*n))
pattern=pattern()
pattern.print_pattern(5)