import random

			######################################
			#            The Banners             #
			######################################
			
poster1 = """
		\033[92m1010101010101010101010101010101010101010101010101010
		0101010101010101010101010101010101010101010101010101			
		01\033[31m$$$\033[92m01010\033[31m$$$$$$$\033[92m0\033[31m$$$$$$$\033[92m0\033[31m$$$\033[92m1010101\033[31m$$$\033[92m0\033[31m$$$$$$$$$$\033[92m01
		10\033[31m$$$\033[92m1010\033[31m$$$\033[92m1010\033[31m$$$\033[92m1010\033[31m$$$\033[92m0\033[31m$$$\033[92m10101\033[31m$$$\033[92m01\033[31m$$$\033[92m010101010
		01\033[31m$$$\033[92m0101\033[31m$$$\033[92m01010\033[31m$\033[92m10101\033[31m$$$\033[92m0\033[31m$$$\033[92m10101\033[31m$$$\033[92m10\033[31m$$$\033[92m101010101
		10\033[31m$$$\033[92m10101\033[31m$$$\033[92m101010101\033[31m$$$\033[92m101\033[31m$$$\033[92m010\033[31m$$$\033[92m101\033[31m$$$$$$$$\033[92m1010
		01\033[31m$$$\033[92m010101\033[31m$$$\033[92m1010101\033[31m$$$\033[92m10101\033[31m$$$\033[92m0\033[31m$$$\033[92m1010\033[31m$$$\033[92m101010101
		10\033[31m$$$\033[92m1010101\033[31m$$$\033[92m01010\033[31m$$$\033[92m010101\033[31m$$$\033[92m0\033[31m$$$\033[92m0101\033[31m$$$\033[92m010101010
		01\033[31m$$$$$$$$$\033[92m010\033[31m$$$$$$$\033[92m010101010\033[31m$$$$$\033[92m10101\033[31m$$$$$$$$$$\033[92m01		
		\033[92m1010101010101010101010101010101010101010101010101010
		0101010101010101010101010101010101010101010101010101\033[0m		


\t\t\t\b\b""\033[33m\033[04mCreated with love by: Nishant Senchua\033[33m\033[0m\n\t\t\t\033[33m\033[04mDate: Aug 20, 2020\033[0m\n\t\t\t\033[33m\033[04mVersion: 1.0\n\t\t\t\033[33m\033[04mEmail: root.user744@gmail.com\033[0m\n\t\t\t\033[33m\033[04mGithub: root-user744\033[0m""
"""
poster2 = """
           The \033[32m███╗░░░███╗░█████╗░████████╗██╗░░██╗
	       ████╗░████║██╔══██╗╚══██╔══╝██║░░██║
 	       ██╔████╔██║███████║░░░██║░░░███████║
     	       ██║╚██╔╝██║██╔══██║░░░██║░░░██╔══██║
               ██║░╚═╝░██║██║░░██║░░░██║░░░██║░░██║
               \033[32m╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝\033[0m Shell.
	      (Only Mathematical commands available)	

	      ""\033[33m\033[04mCreated with love by: Nishant Senchua\033[33m\033[0m\n\t\t\033[33m\033[04mDate: Aug 20, 2020\033[0m\n\t\t\033[33m\033[04mVersion: 1.0\n\t\t\033[33m\033[04mEmail: root.user744@gmail.com\033[0m\n\t\t\033[33m\033[04mGithub: root-user744\033[0m""
"""

poster3 = """
\033[37m────────────────(\033[31m♥\033[37m)(\033[31m♥\033[37m)(\033[31m♥\033[37m)───(\033[31m♥\033[37m)(\033[31m♥\033[37m)(\033[31m♥\033[37m)__ \033[92m(a + b)² = a² + 2ab + b² 
\033[37m──────────────(\033[31m♥\033[37m)01010(\033[31m♥\033[37m)(\033[31m♥\033[37m)1010100(\033[31m♥\033[37m)\033[92m (a - b)² = a² - 2ab + b² 
\033[37m─────────────(\033[31m♥\033[37m)10101010(\033[31m♥\033[37m)101010101(\033[31m♥\033[37m)──\033[92m a² - b² = (a + b) (a - b)
\033[37m─────────────(\033[31m♥\033[37m)101\033[31mTHE\033[37m0\033[31mMATH\033[37m0\033[31mSHELL\033[37m10(\033[31m♥\033[37m)\033[92m (√2 x √2) + 2  = 2 x 2
\033[37m──────────────(\033[31m♥\033[37m)10101010101010101(\033[31m♥\033[37m)── \033[92msin²θ + cos²θ = 1
\033[37m────────────────(\033[31m♥\033[37m)1010101010101(\033[31m♥\033[37m)\033[92m tan²θ + 1 = sec²θ  
\033[37m──────────────────(\033[31m♥\033[37m)0101010101(\033[31m♥\033[37m)──\033[92m cot²θ + 1 = cosec²θ
\033[37m────────────────────(\033[31m♥\033[37m)101010(\033[31m♥\033[37m)\033[92m π = 3.1415926535897....
\033[37m─────────────────────(\033[31m♥\033[37m)010(\033[31m♥\033[37m)──\033[92m a = πr²
\033[37m──────────────────────(\033[31m♥\033[37m)0(\033[31m♥\033[37m)\033[92m e = mc²
\033[37m────────────────────────(\033[31m♥\033[37m)── \033[92m∞\033[0m

\t\t\b\b""\033[33m\033[04mCreated with love by: Nishant Senchua\033[33m\033[0m\n\t\t\033[33m\033[04mDate: Aug 20, 2020\033[0m\n\t\t\033[33m\033[04mVersion: 1.0\n\t\t\033[33m\033[04mEmail: root.user744@gmail.com\033[0m\n\t\t\033[33m\033[04mGithub: root-user744\033[0m""
"""

poster4 = """"""
poster5 = """"""
poster6 = """"""
poster7 = """"""
poster8 = """"""
poster9 = """"""
poster10 = """"""

			############################################################################################
			#              The function to display a different poster each time the user               #
			#	       runs the program or gives the banner command.                               #
			############################################################################################
      
def banner():
	posters = [poster1, poster2, poster3] #poster4, poster5, poster6, poster7, poster8, poster9, poster10]
	random.shuffle(posters)
	return posters[1]

