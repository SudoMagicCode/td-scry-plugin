# me - this DAT
# scriptOp - the OP which is cooking
#
# press 'Setup Parameters' in the OP to call this function to re-create the parameters.
def onSetupParameters(scriptOp):
    page = scriptOp.appendCustomPage('Custom')
    p = page.appendFloat('Valuea', label='Value A')
    p = page.appendFloat('Valueb', label='Value B')
    return

# called whenever custom pulse parameter is pushed


def onPulse(par):
    return


def onCook(scriptOp):
    scriptOp.clear()
    rows: list = []

    header: list = ['wsConnection']
    rows.append(header)

    for each in parent.scry.Web_server_DAT.webSocketConnections:
        rows.append([each])

    for eachRow in rows:
        scriptOp.appendRow(eachRow)

    # scriptOp.copy(scriptOp.inputs[0])	# no need to call .clear() above when copying
    # scriptOp.insertRow(['color', 'size', 'shape'], 0)
    # scriptOp.appendRow(['red', '3', 'square'])
    # scriptOp[1,0] += '**'

    return


def onGetCookLevel(scriptOp):
    """
    sets the scriptOp's cook level, the conditions necessary to cause a cook.

    Return one of the following:
            CookLevel.AUTOMATIC - inputs changed and output being used. TD default behavior.
            CookLevel.ON_CHANGE - inputs changed, output used or not.
            CookLevel.WHEN_USED - every frame when output is being used
            CookLevel.ALWAYS - every frame
    """

    return CookLevel.AUTOMATIC
