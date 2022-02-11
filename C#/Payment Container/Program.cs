namespace Payment_Container
{
    using System;

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            Container container = new Container("payments.txt");

            Console.WriteLine(container);
            //container.WriteToFile();

            Console.WriteLine("Bye World!");
        }
    }
}
