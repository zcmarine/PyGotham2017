#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule


def setup_module():
    return AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str'),
        ),
        supports_check_mode=True
    )


def main():
    module = setup_module()

    if module.check_mode:
        module.exit_json(changed=False, msg='This is check mode')

    if module.params['name'] == 'Oscar':
        module.fail_json(msg="Don't use the name 'Oscar'")

    module.exit_json(changed=True, msg=module.params['name'])


if __name__ == '__main__':
    main()
