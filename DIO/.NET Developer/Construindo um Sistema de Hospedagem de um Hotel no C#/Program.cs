using System.Net.Http.Headers;

public class Program
{
    public static void Main()
    {
        // Exemplo de uso do sistema

        // Cria algumas instâncias de Pessoa
        Pessoa pessoa1 = new Pessoa("Alice", "Alcantara");
        Pessoa pessoa2 = new Pessoa("Victor", "Ribeiro");

        // Cria uma instância de Suite
        Suite suite = new Suite("Luxo", 2, 150.00m);

        // Cria uma instância de Reserva e associa a suite
        Reserva reserva = new Reserva();
        reserva.SuiteReservada = suite;
        reserva.DiasReservados = 12;

        // Adiciona hóspedes à reserva
        reserva.AdicionarHospede(pessoa1);
        reserva.AdicionarHospede(pessoa2);

        // Exibe a quantidade de hóspedes
        Console.WriteLine("Quantidade de Hóspedes: " + reserva.ObterQuantidadeHospedes());

        // Calcula e exibe o valor da diária
        Console.WriteLine("Valor Total da Diária: " + reserva.CalcularValorDiaria());
    }
}