namespace Payment_Container
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Reflection;

    class Container
    {
        private string _filename;
        public List<PaymentModel> Payments { get; private set; }

        public int Count() => Payments.Count;

        public Container(string filename)
        {
            SetFileName(filename);
            Payments = new List<PaymentModel>();
            ReadFromFile();
        }

        public void ReadFromFile()
        {
            StreamReader file = new StreamReader(Services.PathProject + "payments.txt");
            int numberOfPayment = 1;

            while (!file.EndOfStream)
            {
                var propertiesDictionary = new Dictionary<string, string>();
                var line = file.ReadLine().Split(": ");
                if (line[0] == "") break;
                while (line[0][0] != '=')
                {
                    propertiesDictionary.Add(line[0], line[1]);
                    line = file.ReadLine().Split(": ");
                }

                var payment = new PaymentModel();
                var errors = this.Deserialize(propertiesDictionary, payment);

                if (errors.Count > 0)
                {
                    Console.WriteLine($"Payment number {numberOfPayment} is defective!!!\n  Errors: {errors.Count}");
                    for (int i = 1; i <= errors.Count; ++i)
                        Console.WriteLine($">>> {i}. {errors[i - 1]}");
                    Console.WriteLine("------------------------------------------------------");
                }
                else
                    Payments.Add(payment);

                numberOfPayment++;
            }
            file.Close();
        }

        public async void WriteToFile()
        {
            StreamWriter sw = new StreamWriter(Services.PathProject + _filename, false);
            await sw.WriteLineAsync(this.ToString());
            sw.Close();
        }

        public override string ToString()
        {
            string payments = String.Empty;
            foreach (var payment in Payments)
                payments += payment.ToString() + "============================\n";
            return payments;
        }

        public void SetFileName(string filename)
            => _filename = filename;

        private List<string> Deserialize(Dictionary<string, string> propertiesDictionary, PaymentModel payment)
        {
            PropertyInfo[] properties = Services.GetPropertiesClassPaymentService();
            List<string> errors = new List<string>();

            for (int i = 0; i < properties.Length; i++)
            {
                try
                {
                    properties[i].SetValue(payment, propertiesDictionary[properties[i].Name]);
                }
                catch (Exception ex)
                {
                    if (ex.InnerException != null)
                        errors.Add($"{ex.InnerException.Message}");
                    else
                        errors.Add($"{ex.Message}");
                }
            }

            return errors;
        }
    }
}