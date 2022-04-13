class StringUtility:

 def __init__ (self,string):
   self.string = string

 def __str__ (self):
   return self.string

 def vowels(self):
   count=0
   vowels=set("AEIOUaeiou")
   for i in self.string:
    if i in vowels:
      count+=1
    if count>=5:
      return "many"
   return str(count)

 def bothEnds(self):
     if len(self.string)<=2:
       return""
     else:
       return self.string[0:2]+self.string[-2:]

 def fixStart(self):
   if len(self.string)<=1:
     return""
   else:
     return self.string[0]+self.string[1:].replace(self.string[0],'*')

 def asciiSum(self):
   ascii_sum=0
   for i in self.string:
     ascii_sum+=(ord(i))
   return ascii_sum

 def cipher(self):
   cipher=""
   cipher_shift=len(self.string)
   for character in self.string:
     if character.isupper():
       alphabet=ord(character)-ord('A')
       alphabet_shift=(alphabet+cipher_shift)%26+ord('A')
       new_character=chr(alphabet_shift)
       cipher+=new_character
     elif character.islower():
       alphabet=ord(character)-ord('a')
       alphabet_shift=(alphabet+cipher_shift)%26+ord('a')
       new_character=chr(alphabet_shift)
       cipher+=new_character
     else:
       cipher+=character
   return cipher

  
      