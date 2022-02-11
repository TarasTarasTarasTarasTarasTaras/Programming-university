namespace Payment_Container
{
    using System;
    using static Validation.Payment;

    class PaymentModel
    {
        private int _id;
        private decimal _amount;
        private string _currency;
        private string _payerEmail;
        private DateTime _requestDate;
        private DateTime _dueToDate;
        private string _transactionId;

        public string Id             { get => _id.ToString();              set { _id = ValidateId(value); }}
        public string Amount         { get => _amount.ToString();          set { _amount = ValidateAmount(value); }}
        public string Currency       { get => _currency;                   set { _currency = ValidateCurrency(value); }}
        public string PayerEmail     { get => _payerEmail;                 set { _payerEmail = ValidateEmail(value); }}
        public string RequestDate    { get => _requestDate.ToString("d");  set { _requestDate = ValidateRequestDate(value); }}
        public string DueToDate      { get => _dueToDate.ToString("d");    set { _dueToDate = ValidateDueToDate(value, _requestDate); }}
        public string TransactionId  { get => _transactionId;              set { _transactionId = ValidateTransactionId(value); }}

        public override string ToString()
        {
            var properties = Services.GetPropertiesClassPaymentService();

            string payments = String.Empty;

            foreach (var property in properties)
                payments += $"{property.Name}: {property.GetValue(this)}\n";

            return payments;
        }
    }
}