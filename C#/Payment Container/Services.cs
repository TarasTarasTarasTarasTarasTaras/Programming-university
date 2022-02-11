namespace Payment_Container
{
    using System;
    using System.Collections.Generic;
    using System.Reflection;
    using System.Text;

    static class Services
    {
        public static string PathProject { get; } = @"D:\C# university\Payment Container\Payment Container\";

        public static PropertyInfo[] GetPropertiesClassPaymentService()
        {
            PropertyInfo[] propertyInfo;
            Type type = typeof(PaymentModel);
            propertyInfo = type.GetProperties();
            return propertyInfo;
        }
    }
}
