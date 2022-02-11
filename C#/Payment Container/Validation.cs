namespace Payment_Container
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Text;
    using System.Text.RegularExpressions;

    class Validation
    {
        public static class Payment
        {
            private static string[] _allowedCurrencies = new string[] { "usd", "eur", "uah" };
            private static string _patternEmail = @"^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$";
            private static string _patternTransactionId = @"^\d{8}-\d{2}$";

            public static int ValidateId(string _id)
            {
                int id;
                try
                {
                    id = int.Parse(_id);
                }
                catch
                {
                    throw new BadPaymentException("Id must be integer");
                }
                if (id < 0 || id > 10000000)
                    throw new BadPaymentException("Id must be positive or 0 and less than 10000000");
                return id;
            }

            public static decimal ValidateAmount(string _amount)
            {
                decimal amount;
                try
                {
                    amount = decimal.Parse(_amount);
                }
                catch
                {
                    throw new BadPaymentException("Amount must be decimal");
                }
                if (amount <= 0 || amount > 10000000)
                    throw new BadPaymentException("Amount must be positive and less than 10000000");
                return amount;
            }

            public static string ValidateCurrency(string currency)
            {
                if(_allowedCurrencies.FirstOrDefault(c => c == currency) is null)
                    throw new BadPaymentException("Incorrect currency specified");
                return currency;
            }

            public static string ValidateEmail(string email)
            {
                if (!Regex.IsMatch(email, _patternEmail))
                    throw new BadPaymentException("Bad email format");
                return email;
            }

            public static DateTime ValidateRequestDate(string _requestDate)
            {
                DateTime requestDate;
                try
                {
                    requestDate = DateTime.Parse(_requestDate);
                }
                catch (FormatException)
                {
                    throw new BadPaymentException("Bad request date format");
                }
                if(requestDate.Year < 1980) 
                    throw new BadPaymentException("The year of the date of the request cannot be less than 1980");
                if(requestDate > DateTime.Now)
                    throw new BadPaymentException($"The date of the request cannot be later {DateTime.Now.ToString("d")}");

                return requestDate;
            }

            public static DateTime ValidateDueToDate(string _dueToDate, DateTime requestDate)
            {
                DateTime dueToDate;
                try
                {
                    dueToDate = DateTime.Parse(_dueToDate);
                }
                catch (FormatException)
                {
                    throw new BadPaymentException("Bad request date format");
                }
                if (dueToDate.Year < 1980)
                    throw new BadPaymentException("The year of the due to date cannot be less than 1980");
                if (dueToDate < requestDate)
                    throw new BadPaymentException("Request date must be earlier than due to date");

                return dueToDate;
            }

            public static string ValidateTransactionId(string transactionId)
            {
                if (!Regex.IsMatch(transactionId, _patternTransactionId))
                    throw new BadPaymentException("Bad TransactionId format. Must be: ********-** and contain only numbers");

                return transactionId;
            }
        }
    }
}