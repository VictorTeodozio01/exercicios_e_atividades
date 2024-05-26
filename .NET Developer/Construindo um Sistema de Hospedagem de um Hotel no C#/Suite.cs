public class Suite
{
    public string TipoSuite { get; set; }
    public int Capacidade { get; set; }
    public decimal ValorDiaria { get; set; }

    public Suite(string tiposuite, int capacidade, decimal valorDiaria)
    {
        TipoSuite = tiposuite;
        Capacidade = capacidade;
        ValorDiaria = valorDiaria;
    }
}