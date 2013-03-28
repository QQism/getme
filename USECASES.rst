=========
Use cases
=========


String
######

::
    <div id='content'>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>

Input ::
    <div id='content'><getme/></div>

Ouput ::
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

List
####

::
    <ul>
        <li>One</li>
        <li>Two</li>
        <li>Three</li>
    </ul>

Input ::
    <ul>
        <li><getme/></li>
    </ul>

Output ::
    ['One', 'Two', 'Three']

Table
#####

::
    <table>
        <thead></thead>
        <tbody>
            <tr>
                <td>Quang</td>
                <td>Quach</td>
                <td>1989</td>
                <td>HCMC</td>
            </tr>
            <tr>
                <td>Yen</td>
                <td>Quach</td>
                <td>1958</td>
                <td>HCMC</td>
            </tr>
            <tr>
                <td>Xuan</td>
                <td>Bui</td>
                <td>1989</td>
                <td>Dong Nai</td>
            </tr>
        </tbody>
        <tfoot></tfoot>
    </table>

Input ::
    <table>
        <tbody>
            <getme group='person'>
                <tr>
                    <td><getme/></td>
                </tr>
            </getme>
        </tbody>
    </table>

Ouput ::
    [{'person': ['Quang', 'Quach', '1989', 'HCMC']},
    {'person': ['Yen', 'Quach', '1958', 'HCMC']},
    {'person': ['Xuan', 'Bui', '1989', 'Dong Nai']}]
