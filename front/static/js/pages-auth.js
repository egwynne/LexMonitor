/**
 *  Pages Authentication
 */

'use strict';
const formAuthentication = document.querySelector('#formAuthentication');

document.addEventListener('DOMContentLoaded', function (e) {
  (function () {
    // Form validation for Add new record
    if (formAuthentication) {
      const fv = FormValidation.formValidation(formAuthentication, {
        fields: {
          nombre: {
            validators: {
              notEmpty: {
                message: 'Ingrese su nombre'
              }
            }
          },
          username: {
            validators: {
              notEmpty: {
                message: 'Ingrese usuario'
              },
              stringLength: {
                min: 6,
                message: 'Usuario debe contener mas de 6 caracteres'
              }
            }
          },
          email: {
            validators: {
              notEmpty: {
                message: 'Ingrese su correo'
              },
              emailAddress: {
                message: 'Ingrese una direccion de correo valida'
              }
            }
          },
          'email-username': {
            validators: {
              notEmpty: {
                message: 'Please enter email / username'
              },
              stringLength: {
                min: 6,
                message: 'Username must be more than 6 characters'
              }
            }
          },
          password: {
            validators: {
              notEmpty: {
                message: 'Ingrese una contraseña'
              },
              stringLength: {
                min: 6,
                message: 'La contraseña debe contener mas de 6 caracteres'
              }
            }
          },
          'confirm-password': {
            validators: {
              notEmpty: {
                message: 'Porfavor confirme contraseña'
              },
              identical: {
                compare: function () {
                  return formAuthentication.querySelector('[name="password"]').value;
                },
                message: 'Las contraseñas no son iguales'
              }
            }
          },
          terms: {
            validators: {
              notEmpty: {
                message: 'Debe aceptar terminos y condiciones'
              }
            }
          },
          
          apellido: {
            validators: {
              notEmpty: {
                message: 'Ingrese su apellido'
              }
            }
          },
          empresa: {
            validators: {
              notEmpty: {
                message: 'Ingrese el nombre de su Empresa'
              }
            }
          },
          'razon_social': {
            validators: {
              notEmpty: {
                message: 'Ingrese su Razon Social'
              }
            }
          },
          rut: {
            validators: {
              notEmpty: {
                message: 'Ingrese su Rut'
              }
            }
          }
        },
        plugins: {
          trigger: new FormValidation.plugins.Trigger(),
          bootstrap5: new FormValidation.plugins.Bootstrap5({
            eleValidClass: '',
            rowSelector: '.mb-3'
          }),
          submitButton: new FormValidation.plugins.SubmitButton(),

          defaultSubmit: new FormValidation.plugins.DefaultSubmit(),
          autoFocus: new FormValidation.plugins.AutoFocus()
        },
        init: instance => {
          instance.on('plugins.message.placed', function (e) {
            if (e.element.parentElement.classList.contains('input-group')) {
              e.element.parentElement.insertAdjacentElement('afterend', e.messageElement);
            }
          });
        }
      });
    }

    //  Two Steps Verification
    const numeralMask = document.querySelectorAll('.numeral-mask');

    // Verification masking
    if (numeralMask.length) {
      numeralMask.forEach(e => {
        new Cleave(e, {
          numeral: true
        });
      });
    }
  })();
});
