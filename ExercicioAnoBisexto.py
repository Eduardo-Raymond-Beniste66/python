def bissexto():

   ano = input ('ano:')

   if ano/4 == True:
       if ano/100 == True:
           if ano/400 == True:
               print ('bissexto')
           else:
               print('nao bissexto')
       else:
           print('bissexto')
   else:
       print('nao bissexto')

if __name__=='__main__':
   bissexto()
