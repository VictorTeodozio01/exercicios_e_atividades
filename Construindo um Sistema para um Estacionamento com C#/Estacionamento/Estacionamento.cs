using System;
using System.Collections.Generic;

public class Estacionamento
{
    private decimal precoInicial;
    private decimal precoPorHora;
    private List<string> veiculos = new List<string>();

    public Estacionamento(decimal precoInicial, decimal precoPorHora)
    {
        this.precoInicial = precoInicial;
        this.precoPorHora = precoPorHora;
    }

    public void AdicionarVeiculo()
    {
        Console.Write("Digite a placa do veículo para estacionar: ");
        string placa = Console.ReadLine();
        veiculos.Add(placa);
        Console.WriteLine("Veículo adicionado com sucesso.");
    }

    public void RemoverVeiculo()
    {
        Console.Write("Digite a placa do veículo para remover: ");
        string placa = Console.ReadLine();

        if (veiculos.Contains(placa))
        {
            Console.Write("Digite a quantidade de horas que o veículo permaneceu estacionado: ");
            int horas = int.Parse(Console.ReadLine());

            decimal valorTotal = precoInicial + precoPorHora * horas;
            veiculos.Remove(placa);
            Console.WriteLine($"O veículo {placa} foi removido e o preço total foi de: R$ {valorTotal}");
        }
        else
        {
            Console.WriteLine("Desculpe, esse veículo não está estacionado aqui. Confira se digitou a placa corretamente.");
        }
    }

    public void ListarVeiculos()
    {
        if (veiculos.Count > 0)
        {
            Console.WriteLine("Os veículos estacionados são:");
            foreach (var veiculo in veiculos)
            {
                Console.WriteLine(veiculo);
            }
        }
        else
        {
            Console.WriteLine("Não há veículos estacionados.");
        }
    }
}
