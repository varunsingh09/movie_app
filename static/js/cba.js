$(document).ready(function () {
 
window.setTimeout(function() {

    $(".alert").fadeTo(1500, 0).slideUp(500, function(){

        $(this).remove(); 
    });

}, 5000),



//Data tables init

$('#locations').DataTable(),
$('#chartsOfAccounts').DataTable(),
$('#accounts').DataTable(),
$('#banks').DataTable(),
$('#currencies').DataTable(),
$('#legal_entities').DataTable(),
$('#business_partners').DataTable(),
$('#calendars').DataTable(),
$('#periods').DataTable(),
$('#taxes').DataTable(),
$('#journals').DataTable(),
$('#journalDetails').DataTable(),
$('#budgets').DataTable(),
$('#budgetDetails').DataTable(),
$('#rates').DataTable(),
$('#item_category').DataTable(),
$('#items').DataTable(),
$('#requestForQuotes').DataTable(),
$('#rfqDetails').DataTable(),
$('#purchaseOrders').DataTable(),
$('#purchaseOrderDetails').DataTable(),
$('#goodsReceipts').DataTable(),
$('#goodsReceiptDetails').DataTable(),
$('#bills').DataTable(),
$('#billDetails').DataTable(),
$('#quotes').DataTable(),
$('#quoteDetails').DataTable(),
$('#saleOrders').DataTable(),
$('#saleOrderDetails').DataTable(),
$('#shippings').DataTable(),
$('#shippingDetails').DataTable(),
$('#invoices').DataTable(),
$('#invoiceDetails').DataTable(),

 // Adding validation to forms
  $('#locationForm').validate({

    rules: {

        'street': {

          required: true,
          minlength: 3

        },

        'city': {

          required: true,
          minlength: 3

        }
     },

    messages: {

        'street': {
    
          minlength: "Please enter a street with at least 3 characters"
        },

        'city': {
    
          minlength: "Please enter a city with at least 3 characters"
        }

    },

    highlight: function(element) {
                $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },

    success: function(element) {
                $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },

    errorClass: 'help-block'
    
  }),

  $('#bankForm').validate({ 

    rules: {

        'code': {

          required: true,
          minlength: 3

        },

        'bank': {

          required: true,
          minlength: 5

        }
     },

    messages: {

        'code': {
    
          minlength: "Please enter a code with at least 3 characters"
        },

        'bank': {
    
          minlength: "Please enter a bank name with at least 4 characters"
        }

    },

    highlight: function(element) {
                $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },

    success: function(element) {
                $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },

    errorClass: 'help-block'
    
  }),
 
  $('#chartOfAccountsForm').validate({

    rules: {

        'code': {

          required: true,
          minlength: 3

        },

        'chart': {

          required: true,
          minlength: 4

        }
     },

   	messages: {

		    'code': {
		
			    minlength: "Please enter a code with at least 3 characters"

		    },

        'chart': {
    
          minlength: "Please enter a chart with at least 4 characters"
          
        }

    },

    highlight: function(element) {
                $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },

    success: function(element) {
                $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },

    errorClass: 'help-block'
    
  }),

  
  $('#accountForm').validate({

    rules: {

        'code': {

          required: true,
        },

        'account': {

          required: true,
          minlength: 5

        }
     },

   	messages: {

		    'account': {
		
			    minlength: "Please enter an account name with at least 5 characters"
		    }

    },

    highlight: function(element) {
                $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },

    success: function(element) {
                $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },

    errorClass: 'help-block'
    
  }),
  

  $('#legalEntityForm').validate({

    rules: {

        'code': {

          required: true,
          minlength: 3

        },

        'entity': {

          required: true,
          minlength: 5

        }

    },

   	messages: {

		    'code': {
		
			    minlength: "Please enter a code with at least 3 characters"
		    
        },

		    'entity': {
		
			   minlength: "Please enter an entity name with at least 5 characters"

		    },
		    
    },

    highlight: function(element) {
                $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },

    success: function(element) {
                $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },

    errorClass: 'help-block'
    
  }),


  $('#calendarForm').validate({

    rules: {

        'calendar': {

          required: true,
          minlength: 4

        },

        'year': {

          required: true,
          minlength: 4

        },

     },

   	messages: {

		    'calendar': {
		
			    minlength: "Please enter a calendar name with at least 4 characters"
		    },

		    'year': {
		
			    minlength: "Please enter a correct year (e.g 2016,2017...)"
		    },

    },

    highlight: function(element) {
                $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },

    success: function(element) {
                $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },

    errorClass: 'help-block'
    
  }),


$('#periodForm').validate({

    rules: {

        'period': {

          required: true,
          minlength: 3

        },

        'period_start': {

          required: true,
          minlength: 6

        },

        'period_end': {

          required: true,
          minlength: 6

        }


     },

   	messages: {

		    'period': {
		
			    minlength: "Please enter a period name with at least 5 characters"
		    },

		    'period_start': {
		
			    minlength: "Please enter a correct date"
		    },

		    'period_end': {
		
			    minlength: "Please enter a correct date"
		    }

    },

    highlight: function(element) {
                $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },

    success: function(element) {
                $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },

    errorClass: 'help-block'
    
  }),  



 $('#taxForm').validate({

    rules: {

        'code': {

          required: true,
          minlength: 3

        },

        'tax': {

          required: true,
          minlength: 3

        },

        'start_date': {

          required: true,
          minlength: 6

        },

        'end_date': {

          required: true,
          minlength: 6

        }

     },

    messages: {

        'code': {
    
          minlength: "Please enter a code with at least 3 characters"
    
        },

        'tax': {
    
          minlength: "Please enter a name with at least 5 characters"
      
        },

        'type': {
           
      
        },

        'start_date': {
    
          minlength: "Please enter a correct date"
      
        },

        'end_date': {
    
         minlength: "Please enter a correct date"
      
        }
    
    }, 

    highlight: function(element) {
                $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },

    success: function(element) {
                $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },

    errorClass: 'help-block'
    
  }),     

  $('#journalForm').validate({

    rules: {

        'memo': {

          required: true,
          minlength: 5

        }

   },

   messages: {

		    'memo': {
		
			    minlength: "Please enter a memo with at least 5 characters"
		  
        }
 
	 	    
    },

    highlight: function(element) {
                $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },

    success: function(element) {
                $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },

    errorClass: 'help-block'
    
  }),
 
  $('#journalDetailsForm').validate({

    rules: {

        'amount': {

          required: true,
          minlength: 2

        },
     },

   	messages: {

		    'amount': {
		
			    minlength: "The amount field must have at least 2 characters"
		    },
    	 	    
    },

    highlight: function(element) {
                $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },

    success: function(element) {
                $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },

    errorClass: 'help-block'
    
  }),

  $('#budgetForm').validate({

    rules: {

        'budget': {

          required: true,
          minlength: 3

        },

     },

   	messages: {

		    'budget': {
		
			    minlength: "The budget field must have at least 3 characters"
		    },
	 	    
    },

    highlight: function(element) {
                $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },

    success: function(element) {
                $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },

    errorClass: 'help-block'
    
  }),

  $('#budgetDetailsForm').validate({

    rules: {

        'amount': {

          required: true,
          minlength: 2

        },

     },

   	messages: {

		    'amount': {
		
			    minlength: "The amount field must have at least 2 characters"
		    },
  
	 	    
    },

    highlight: function(element) {
                $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },

    success: function(element) {
                $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },

    errorClass: 'help-block'
    
  }),

  $('#businessPartnerForm').validate({

    rules: {

        'code': {

          required: true,
          minlength: 3

        },

        'business_partner': {

          required: true,
          minlength: 3

        },

     },

    messages: {

        'code': {
    
          minlength: "Please enter a code with at least 3 characters"
 
        },
    
        'business_partner': {
    
          minlength: "Please enter a name with at least 3 characters"
      
        },

    },

    highlight: function(element) {
                $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },

    success: function(element) {
                $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },

    errorClass: 'help-block'
    
  }),

  $('#businessPartnerAddressForm').validate({

    rules: {

        'city': {

          required: true,
          minlength: 3

        },

        'street': {

          required: true,
          minlength: 5

        },

        'state_province': {

          required: true,
          minlength: 3

        },

     },

    messages: {

        'city': {
    
          minlength: "Please enter a city name with at least 3 characters"
 
        },
    
        'street': {
    
          minlength: "Please enter an address with at least 5 characters"
      
        },

        'state_province': {

          minlength: "Please enter an address with at least 3 characters"

        },

    },

    highlight: function(element) {
                $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },

    success: function(element) {
                $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },

    errorClass: 'help-block'
    
  }),

  $('#itemCategoryForm').validate({

    rules: {

        'category': {

          required: true,
          minlength: 3

        },
     },

    messages: {

        'category': {
    
          minlength: "Please enter a name with at least 3 characters"
 
        },

    },

    highlight: function(element) {
                $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },

    success: function(element) {
                $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },

    errorClass: 'help-block'
    
  }),

  
  $('#itemForm').validate({

    rules: {

        'code': {

          required: true,
          minlength: 3

        },
        
        'item': {

            required: true,
            minlength: 3

        },

     },

    messages: {

        'code': {
    
          minlength: "Please enter a name with at least 3 characters"
 
        },
    
        'item': {
    
          minlength: "Please enter a name with at least 3 characters"
      
        },

    },

    highlight: function(element) {
                $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },

    success: function(element) {
                $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },

    errorClass: 'help-block'
    
    ,
    
  });

});