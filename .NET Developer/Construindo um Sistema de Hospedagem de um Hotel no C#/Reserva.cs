public class Reserva
{
    public List<Pessoa> Hospedes { get; set; }
    public Suite SuiteReservada { get; set; }
    public int DiasReservados { get; set; }

    public Reserva()
    {
        Hospedes = new List<Pessoa>();
    }

    public void AdicionarHospede(Pessoa hospede)
    {
        if (Hospedes.Count >= SuiteReservada.Capacidade)
        {
            throw new Exception("A capacidade da suíte não é suficiente para o número de hóspedes.");
        }
        Hospedes.Add(hospede);
    }

    public int ObterQuantidadeHospedes()
    {
        return Hospedes.Count;
    }

    public decimal CalcularValorDiaria()
    {
        decimal valorTotal = DiasReservados * SuiteReservada.ValorDiaria;

        if (DiasReservados >= 10)
        {
            valorTotal *= 0.90m; // Concede 10% de desconto
        }

        return valorTotal;
    }
}
