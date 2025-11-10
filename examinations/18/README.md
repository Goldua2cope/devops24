# Examination 18 - Write an Ansible module (VG)

Ansible modules are types of plugins that execute automation tasks on a 'target'. In the previous
examinations you have used many different modules, written by Ansible developers.

A module in Ansible is a Python script that adheres to a particular convention.

You can see the places where Ansible looks for modules by dumping the Ansible configuration
and then search for `DEFAULT_MODULE_PATH`:

    $ ansible-config dump | grep -i module_path

We will now write our own module, and run it through Ansible.

# QUESTION A

Look at [Developing modules](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html)
and create a module that
f
* Is called `anagrammer`
* Takes one parameter, `message`, that is a string.
* Returns two values:
    - `original_message` that is the string that is passed through `message`
    - `reversed_message` that is the `message` string, only backwards (reversed).
* If the `original_message` and `reversed_message` is different, the `changed` parameter should be `True`, otherwise
  it should be `False`.

When you are done, you should be able to do

    $ ANSIBLE_LIBRARY=./library ansible -m anagrammer -a 'message="hello world"' localhost

And it should return

    localhost | CHANGED => {
        "changed": true,
        "original_message": "hello world",
        "reversed_message": "dlrow olleh"
    }

You should also be able to do

    ANSIBLE_LIBRARY=./library ansible -m anagrammer -a 'message="sirap i paris"' localhost

And it should return

    localhost | SUCCESS => {
        "changed": false,
        "original_message": "sirap i paris",
        "reversed_message": "sirap i paris"
    }

If you pass in 'fail me', it should fail like this:

    localhost | FAILED! => {
        "changed": true,
        "msg": "You requested this to fail",
        "original_message": "fail me",
        "reversed_message": "em liaf"
    }

# QUESTION B

Study the output of `ansible-config dump | grep -i module_path`. You will notice that there is a directory
in your home directory that Ansible looks for modules in.

Create that directory, and copy the Ansible module you just wrote there, then make a playbook
that uses this module with the correct parameters.

You don't need to worry about FQCN and namespaces in this examination.

# QUESTION C

Create a playbook called `18-anagrammer.yml` that uses this module.

Make the playbook use a default variable for the message that can be overriden by using something like:

    $ ansible-playbook --verbose --extra-vars message='"This is a whole other message"' 18-custom-module.yml

# BONUS QUESTION

What is the relationship between the booleans you can use in Python, and the various "truthy/falsy" values
you most often use in Ansible?

What modules/filters are there in Ansible that can safely test for "truthy/falsy" values, and return something
more stringent?

Answer:  
In python every value can be evaluated to either true/truthy or false/falsy. Objects are by default considered true unless they are evaluated to false with the __bool__() method or to 0 with the __len__() method. 

Ansible has its own set of values that can be converted into booleans with the bool filter - such as True/yes/on/1 and false/no/off/0. Python wouldn't recognize yes/no or on/off. Ansible has filters that evaluates values pythonically - such as ansible.builtin.falsy and ansible.builtin.truthy. As of Ansible 2.10 ansible allows python like truthy and falsy checks - for example: "when: value is truthy"

These modules/filters that can return more stringent boolean values: ansible.builtin.falsy, ansible.builtin.truthy and ansible.builtin.bool

reference list:
- https://testdriven.io/tips/ba9f859e-ab3d-4ff5-bc44-aebf70b13260/
- https://docs.python.org/3/library/stdtypes.html
- https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/bool_filter.html
- https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/truthy_test.html#ansible-collections-ansible-builtin-truthy-test
- https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_tests.html