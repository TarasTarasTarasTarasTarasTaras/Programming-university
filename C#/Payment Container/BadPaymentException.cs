namespace Payment_Container
{
    using System;
    using System.Runtime.Serialization;

    [Serializable]
    public class BadPaymentException : Exception
    {
        public BadPaymentException() { }

        public BadPaymentException(string message)
            : base(message) { }

        public BadPaymentException(string message, Exception innerException)
            : base(message, innerException) { }

        protected BadPaymentException(SerializationInfo info, StreamingContext context)
            : base(info, context) { }
    }
}