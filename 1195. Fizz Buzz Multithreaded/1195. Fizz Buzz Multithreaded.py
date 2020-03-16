"""
Write a program that outputs the string representation of numbers from 1 to n, however:

If the number is divisible by 3, output "fizz".
If the number is divisible by 5, output "buzz".
If the number is divisible by both 3 and 5, output "fizzbuzz".
For example, for n = 15, we output: 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz.

Suppose you are given the following code:

class FizzBuzz {
  public FizzBuzz(int n) { ... }               // constructor
  public void fizz(printFizz) { ... }          // only output "fizz"
  public void buzz(printBuzz) { ... }          // only output "buzz"
  public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
  public void number(printNumber) { ... }      // only output the numbers
}
Implement a multithreaded version of FizzBuzz with four threads. The same instance of FizzBuzz will be passed to four different threads:

Thread A will call fizz() to check for divisibility of 3 and outputs fizz.
Thread B will call buzz() to check for divisibility of 5 and outputs buzz.
Thread C will call fizzbuzz() to check for divisibility of 3 and 5 and outputs fizzbuzz.
Thread D will call number() which should only output the numbers.
"""
class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.number = threading.Semaphore(0)
        self.fizz = threading.Semaphore(0)
        self.buzz = threading.Semaphore(0)
        self.fizzbuzz = threading.Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        for j in range(self.n//3-self.n//15):
            self.fizz.acquire()
            printFizz()
            self.number.release()
    	

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
    	for j in range(self.n//5-self.n//15):
            self.buzz.acquire()
            printBuzz()
            self.number.release()
    	

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        for j in range(self.n//3-self.n//15):
            self.fizzbuzz.acquire()
            printFizzBuzz()
            self.number.release()
    	

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1,self.n+1):
                self.number.acquire()
                if i % 3 == 0 and i % 5 == 0:
                    self.fizzbuzz.release()
                elif i % 3 == 0:
                    self.fizz.release()
                elif i % 5 == 0:
                    self.buzz.release()
                else:
                    printNumber(i)
                    self.number.release()
        
