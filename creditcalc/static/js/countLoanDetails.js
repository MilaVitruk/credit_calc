var term = document.getElementById("id_term");
            function countTotalMonths(){
            var days = parseInt(term.value.split(" ")[0]);
            var yearsFull = Math.floor(days/365);
            var daysLeft = days - 365 * yearsFull;
            var monthsTotal = yearsFull * 12 + Math.floor(daysLeft / 30.5);
            daysLeft = (daysLeft - monthsTotal % 12) * 30.5;
            if (daysLeft > 0) {
             monthsTotal = monthsTotal + 1
            }

            return monthsTotal;
            }

            function countPaymentPerMonth(){
                var monthsTotal = document.getElementById("id_num_of_payments").value;
                var monthRate = document.getElementById("id_rate").value / (12 * 100);
                var kann = (monthRate*(1+monthRate) ** monthsTotal)/(((1 + monthRate) ** monthsTotal) - 1)
                var paymentPerMonth = document.getElementById("id_amount").value * kann
                return Math.round(paymentPerMonth * 10 ** 2) / 10 ** 2;
    
                }

    term.addEventListener("input", function (e) {
        document.getElementById("id_num_of_payments").value=countTotalMonths();
        document.getElementById("id_payment_per_month").value=countPaymentPerMonth();
        document.getElementById("id_total_amount").value=document.getElementById("id_num_of_payments").value * document.getElementById("id_payment_per_month").value
    
    });