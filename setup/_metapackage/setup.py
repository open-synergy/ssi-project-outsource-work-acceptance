import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-project-outsource-work-acceptance",
    description="Meta package for open-synergy-ssi-project-outsource-work-acceptance Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_project_outsource_work_acceptance',
        'odoo14-addon-ssi_project_outsource_work_acceptance_state_change_constrain',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
