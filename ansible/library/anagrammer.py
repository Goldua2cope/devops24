#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule

def anagrammer():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        message=dict(type='str', rquired=True)
    )

    # dictionary holding result values
    result = dict(
        changed=False,
        original_message='',
        reversed_message=''
    )

    # set module attributes
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # If working with check_mode only return result without changing environment
    if module.check_mode:
        module.exit_json(**result)

    # Define original_message with user input
    # Invert the string and store value as reversed_message
    result['original_message'] = module.params['message']
    result['reversed_message'] = module.params['message'][::-1]

    # Change state if reversal is successful
    if result['original_message'] != result['reversed_message']:
        result['changed'] = True

    if module.params['message'] == 'fail me':
        module.fail_json(msg='You required this to fail', **result)

    # Passing key/value results if module execution successful
    module.exit_json(**result)

def main():
    anagrammer()

if __name__ == '__main__':
    main()