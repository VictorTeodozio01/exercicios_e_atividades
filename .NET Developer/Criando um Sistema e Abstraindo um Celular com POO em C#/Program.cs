using System;
using SmartphoneApp.Models;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Smartphone Nokia:");
        Smartphone nokia = new Nokia("123456", "Nokia 3310", "111111111111111", 64);
        nokia.Ligar();
        nokia.ReceberLigacao();
        nokia.InstalarAplicativo("WhatsApp");

        Console.WriteLine("\nSmartphone iPhone:");
        Smartphone iphone = new Iphone("654321", "iPhone 13", "222222222222222", 256);
        iphone.Ligar();
        iphone.ReceberLigacao();
        iphone.InstalarAplicativo("Telegram");
    }
}
