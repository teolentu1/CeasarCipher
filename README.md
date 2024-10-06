Function breakCipher takes an encrypted string in English made up of the letters a-z and with no spaces. Returns the decrypted string in the same format.

I tried multiple methods to achieve this: searching the shifted string for words in a library and calculating the frequencies of the letters. The first method wasn't effective since it would detect too many "wrong" words in a longer string. A possible way to rectify this is to keep checking if the next charactes after the word are also part of the library, and contine this unitl the string is finished. On the other hand, I found that the frequency method is valid, but only for large texts. 

The method I used in my function uses the most common bigrams and trigrams in the English language. It checks each possible shift of the inputted string, and increases a counter when a bigram or a trigram is found. In the end the shift with the highest counter is outputted, being the english expression we were looking for.  
