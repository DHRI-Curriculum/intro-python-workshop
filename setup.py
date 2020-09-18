from localdjango.setup import read, check_sections_directory, split_into_sections, \
    write_lessons, get_toc, get_nav, insert_get_started_button, slugify, LICENSE, \
    split_frontmatter, split_lessons, get_image_or_title, write_readme


if __name__ == "__main__":

    workshop_title = 'Introduction to Python'

    # setup 'sections' directory
    check_sections_directory()

    frontmatter_sections = split_frontmatter('frontmatter.md')
    contexts = split_into_sections(frontmatter_sections.get("Contexts"), clear_empty_lines=False)

    # split-up + write lesson files
    all_content = split_lessons('lessons.md')
    write_lessons(all_content)

    # generate table of contents
    toc_text = get_toc(all_content, as_dict=False)

    ## README 1. Image / title
    README = get_image_or_title('image.md', workshop_title) + '\n\n'

    ## README 2. Abstract
    README += frontmatter_sections.get("Abstract") + '\n\n'

    ## README 3. Learning objectives
    README += 'In this workshop, you will:\n\n'
    README += frontmatter_sections.get('Learning Objectives') + '\n\n'

    ## README 4. Get started "button"
    README += '---\n\n'
    if frontmatter_sections.get('Estimated time'):
        README += '<p align="center">This workshop is estimated to take you ' + frontmatter_sections.get('Estimated time') + ' to complete.</p>'
    README += insert_get_started_button(url=get_toc(all_content)[1]['path'], center=True)

    ## README 5. Lessons (fka Table of Contents)
    README += '---\n\n'
    README += '## Lessons\n\n'
    README += toc_text + '\n\n'
    README += '---\n\n'

    ## README 6. Contexts/Before you get started
    if frontmatter_sections.get('Prerequisites') or \
        contexts.get('Ethical Considerations') or \
        contexts.get('Pre-reading suggestions') or \
        contexts.get('Projects that use these skills'):
        README += '## Before you get started\n\n'

    if frontmatter_sections.get('Prerequisites'):
        README += f'If you do not have experience or basic knowledge of the following workshops, you may want to look into those before you start with {workshop_title}:\n\n'
        README += frontmatter_sections.get('Prerequisites') + '\n\n'

    if contexts.get('Ethical Considerations'):
        README += '### Ethical Considerations\n\n'
        README += f'Before you start the {workshop_title} workshop, we want to remind you of some ethical considerations to take into account when you read through the lessons of this workshop:\n\n'
        README += contexts.get('Ethical Considerations') + '\n\n'

    if contexts.get('Pre-reading suggestions'):
        README += '### Pre-reading suggestions\n\n'
        README += f'Before you start the {workshop_title} workshop, you may want to read a couple of our pre-reading suggestions:\n\n'
        README += contexts.get('Pre-reading suggestions') + '\n\n'

    if contexts.get('Projects that use these skills'):
        README += '### Projects that use these skills\n\n'
        README += 'You may also want to check out a couple of projects that use the skills discussed in this workshop:\n\n'
        README += contexts.get('Projects that use these skills') + '\n\n'

    # Get started button
    README += '---\n\n'
    README += insert_get_started_button(url=get_toc(all_content)[1]['path'])
    README += '---\n\n'

    ## Acknowledgements
    README += '## Acknowledgements\n\n'
    README += 'This workshop is the result of a collaborative effort of a team of people, mostly involved presently or in the past, with the Graduate Center\'s Digital Initiatives. If you want to see statistics for contributions to this workshop, you can do so [here](https://github.com/DHRI-Curriculum/python/graphs/contributors). This is a list of all the contributors:\n\n'
    README += frontmatter_sections.get("Acknowledgements") + '\n\n'

    ## Licensing information
    README += '---\n\n'
    README += LICENSE + '\n'

    write_readme('README.md', README)