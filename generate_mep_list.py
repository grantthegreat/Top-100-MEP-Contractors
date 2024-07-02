import json

# Data for the top 100 MEP contractors
data = [
    {"Company Name": "AECOM", "Website": "https://www.aecom.com"},
    {"Company Name": "Arup", "Website": "https://www.arup.com"},
    {"Company Name": "Burns & McDonnell", "Website": "https://www.burnsmcd.com"},
    {"Company Name": "Henderson Engineers", "Website": "https://www.hendersonengineers.com"},
    {"Company Name": "IMEG Corp.", "Website": "https://www.imegcorp.com"},
    {"Company Name": "Syska Hennessy Group", "Website": "https://www.syska.com"},
    {"Company Name": "WSP USA", "Website": "https://www.wsp.com"},
    {"Company Name": "Jacobs", "Website": "https://www.jacobs.com"},
    {"Company Name": "Stantec", "Website": "https://www.stantec.com"},
    {"Company Name": "Tetra Tech", "Website": "https://www.tetratech.com"},
    {"Company Name": "DLR Group", "Website": "https://www.dlrgroup.com"},
    {"Company Name": "HDR", "Website": "https://www.hdrinc.com"},
    {"Company Name": "Dewberry", "Website": "https://www.dewberry.com"},
    {"Company Name": "Exp", "Website": "https://www.exp.com"},
    {"Company Name": "Swinerton", "Website": "https://www.swinerton.com"},
    {"Company Name": "Suffolk Construction", "Website": "https://www.suffolk.com"},
    {"Company Name": "The Walsh Group", "Website": "https://www.walshgroup.com"},
    {"Company Name": "Mortenson", "Website": "https://www.mortenson.com"},
    {"Company Name": "Hensel Phelps", "Website": "https://www.henselphelps.com"},
    {"Company Name": "Gilbane Building Company", "Website": "https://www.gilbaneco.com"},
    {"Company Name": "The Whiting-Turner Contracting Company", "Website": "https://www.whiting-turner.com"},
    {"Company Name": "McCarthy Building Companies", "Website": "https://www.mccarthy.com"},
    {"Company Name": "JE Dunn Construction", "Website": "https://www.jedunn.com"},
    {"Company Name": "Brasfield & Gorrie", "Website": "https://www.brasfieldgorrie.com"},
    {"Company Name": "DPR Construction", "Website": "https://www.dpr.com"},
    {"Company Name": "Fluor", "Website": "https://www.fluor.com"},
    {"Company Name": "Balfour Beatty", "Website": "https://www.balfourbeattyus.com"},
    {"Company Name": "Turner Construction", "Website": "https://www.turnerconstruction.com"},
    {"Company Name": "Clark Construction Group", "Website": "https://www.clarkconstruction.com"},
    {"Company Name": "Skanska USA", "Website": "https://www.usa.skanska.com"},
    {"Company Name": "Kiewit Corporation", "Website": "https://www.kiewit.com"},
    {"Company Name": "PCL Construction", "Website": "https://www.pcl.com"},
    {"Company Name": "MasTec", "Website": "https://www.mastec.com"},
    {"Company Name": "Bechtel", "Website": "https://www.bechtel.com"},
    {"Company Name": "KBR", "Website": "https://www.kbr.com"},
    {"Company Name": "Black & Veatch", "Website": "https://www.bv.com"},
    {"Company Name": "Mott MacDonald", "Website": "https://www.mottmac.com"},
    {"Company Name": "LaBella Associates", "Website": "https://www.labellapc.com"},
    {"Company Name": "CDM Smith", "Website": "https://www.cdmsmith.com"},
    {"Company Name": "Gannett Fleming", "Website": "https://www.gannettfleming.com"},
    {"Company Name": "Rogers-O'Brien Construction", "Website": "https://www.r-o.com"},
    {"Company Name": "Zachry Group", "Website": "https://www.zachrygroup.com"},
    {"Company Name": "Granite Construction", "Website": "https://www.graniteconstruction.com"},
    {"Company Name": "Lane Construction Corporation", "Website": "https://www.laneconstruct.com"},
    {"Company Name": "Flatiron Construction", "Website": "https://www.flatironcorp.com"},
    {"Company Name": "Sundt Construction", "Website": "https://www.sundt.com"},
    {"Company Name": "Walbridge", "Website": "https://www.walbridge.com"},
    {"Company Name": "Shawmut Design and Construction", "Website": "https://www.shawmut.com"},
    {"Company Name": "Clayco", "Website": "https://www.claycorp.com"},
    {"Company Name": "Kitchell", "Website": "https://www.kitchell.com"},
    {"Company Name": "Rosendin Electric", "Website": "https://www.rosendin.com"},
    {"Company Name": "M.C. Dean", "Website": "https://www.mcdean.com"},
    {"Company Name": "Faith Technologies", "Website": "https://www.faithtechnologies.com"},
    {"Company Name": "Cupertino Electric", "Website": "https://www.cei.com"},
    {"Company Name": "MYR Group", "Website": "https://www.myrgroup.com"},
    {"Company Name": "IES Holdings", "Website": "https://www.ies-co.com"},
    {"Company Name": "Morrow-Meadows Corporation", "Website": "https://www.morrow-meadows.com"},
    {"Company Name": "Power Design", "Website": "https://www.powerdesigninc.us"},
    {"Company Name": "Miller Electric Company", "Website": "https://www.mecojax.com"},
    {"Company Name": "Bergelectric", "Website": "https://www.bergelectric.com"},
    {"Company Name": "Parsons Corporation", "Website": "https://www.parsons.com"},
    {"Company Name": "Jacobs Engineering Group", "Website": "https://www.jacobs.com"},
    {"Company Name": "Thornton Tomasetti", "Website": "https://www.thorntontomasetti.com"},
    {"Company Name": "Langan Engineering & Environmental Services", "Website": "https://www.langan.com"},
    {"Company Name": "KPFF Consulting Engineers", "Website": "https://www.kpff.com"},
    {"Company Name": "Michael Baker International", "Website": "https://www.mbakerintl.com"},
    {"Company Name": "Terracon Consultants", "Website": "https://www.terracon.com"},
    {"Company Name": "Geosyntec Consultants", "Website": "https://www.geosyntec.com"},
    {"Company Name": "Wood Environment & Infrastructure Solutions", "Website": "https://www.woodplc.com"},
    {"Company Name": "S&ME", "Website": "https://www.smeinc.com"},
    {"Company Name": "TRC Companies", "Website": "https://www.trccompanies.com"},
    {"Company Name": "RS&H", "Website": "https://www.rsandh.com"},
    {"Company Name": "Vanasse Hangen Brustlin (VHB)", "Website": "https://www.vhb.com"},
    {"Company Name": "Kimley-Horn", "Website": "https://www.kimley-horn.com"},
    {"Company Name": "WGI (Wantman Group Inc.)", "Website": "https://www.wginc.com"},
    {"Company Name": "Foth", "Website": "https://www.foth.com"},
    {"Company Name": "Lochner", "Website": "https://www.hwlochner.com"},
    {"Company Name": "Gresham Smith", "Website": "https://www.greshamsmith.com"},
    {"Company Name": "HNTB Corporation", "Website": "https://www.hntb.com"},
    {"Company Name": "STV Group", "Website": "https://www.stvinc.com"},
    {"Company Name": "Maser Consulting", "Website": "https://www.maserconsulting.com"},
    {"Company Name": "Atkins", "Website": "https://www.atkinsglobal.com"},
    {"Company Name": "Woolpert", "Website": "https://www.woolpert.com"},
    {"Company Name": "Psomas", "Website": "https://www.psomas.com"},
    {"Company Name": "Bolton & Menk", "Website": "https://www.bolton-menk.com"},
    {"Company Name": "Consor Engineers", "Website": "https://www.consoreng.com"},
    {"Company Name": "Halff Associates", "Website": "https://www.halff.com"},
    {"Company Name": "MBP", "Website": "https://www.mbpce.com"},
    {"Company Name": "Shive-Hattery", "Website": "https://www.shive-hattery.com"},
    {"Company Name": "CRB", "Website": "https://www.crbusa.com"},
    {"Company Name": "GZA GeoEnvironmental", "Website": "https://www.gza.com"},
    {"Company Name": "Freese and Nichols", "Website": "https://www.freese.com"},
    {"Company Name": "CHA Consulting", "Website": "https://www.cha.com"},
    {"Company Name": "Wiss, Janney, Elstner Associates", "Website": "https://www.wje.com"},
    {"Company Name": "Weston & Sampson", "Website": "https://www.westonandsampson.com"},
    {"Company Name": "Woodard & Curran", "Website": "https://www.woodardcurran.com"},
    {"Company Name": "Kimley-Horn and Associates", "Website": "https://www.kimley-horn.com"},
    {"Company Name": "Sasaki", "Website": "https://www.sasaki.com"},
    {"Company Name": "Sam Schwartz Consulting", "Website": "https://www.samschwartz.com"},
    {"Company Name": "Simpson Gumpertz & Heger", "Website": "https://www.sgh.com"},
    {"Company Name": "WSP Global", "Website": "https://www.wsp.com"},
    {"Company Name": "AECOM Tishman", "Website": "https://www.aecom.com/tishman"},
    {"Company Name": "Hilti North America", "Website": "https://www.hilti.com"},
    {"Company Name": "SGH (Simpson Gumpertz & Heger)", "Website": "https://www.sgh.com"},
    {"Company Name": "Swinerton", "Website": "https://www.swinerton.com"}    {"Company Name": "Swinerton", "Website": "https://www.swinerton.com"}
]

# Generate the HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Top 100 MEP Contractors</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/react/17.0.2/umd/react.production.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/17.0.2/umd/react-dom.production.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.26.0/babel.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css" rel="stylesheet">
</head>
<body>
    <div id="root"></div>

    <script type="text/babel">
        const contractorsData = {json.dumps(data)};

        function App() {
            const [contractors, setContractors] = React.useState(contractorsData);
            const [searchTerm, setSearchTerm] = React.useState('');

            const handleSearch = (event) => {
                const term = event.target.value.toLowerCase();
                setSearchTerm(term);
                const filtered = contractorsData.filter(contractor => 
                    contractor['Company Name'].toLowerCase().includes(term)
                );
                setContractors(filtered);
            };

            return (
                <div className="container mx-auto p-4">
                    <h1 className="text-3xl font-bold mb-4">Top 100 MEP Contractors</h1>
                    <input 
                        type="text" 
                        placeholder="Search companies..." 
                        className="w-full p-2 mb-4 border rounded"
                        value={searchTerm}
                        onChange={handleSearch}
                    />
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                        {contractors.map((contractor, index) => (
                            <div key={index} className="border p-4 rounded shadow">
                                <h2 className="text-xl font-semibold">{contractor['Company Name']}</h2>
                                <a href={contractor['Website']} target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline">
                                    {contractor['Website']}
                                </a>
                            </div>
                        ))}
                    </div>
                </div>
            );
        }

        ReactDOM.render(<App />, document.getElementById('root'));
    </script>
</body>
</html>
"""

# Write the HTML content to a file
with open('index.html', 'w') as f:
    f.write(html_content)

print("HTML file 'index.html' has been generated.")
